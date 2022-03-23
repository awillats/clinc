'''
NOTE: borrowed from https://github.com/awillats/clinc-analysis
'''

from IPython.display import SVG 
import numpy as np
import network_plotting_functions as netplot #only used for circular layout, try to remove?

from PIL import Image
import io
import cairosvg

W = 500 
H = 400 
w = W/2
h = H/2

# %%
'''
set up XML strings for SVG rendering, using python f-strings 
to substitute specified values. 
TODO: would be nice to be able to restyle elements after the fact 
    - perhaps by adding CSS classes?
'''
def gen_canvas(width, height, content, background_color="white"):
    svg_str = f'<svg width="{width}" height="{height}" style="background-color:{background_color}">{content}</svg>'
    return svg_str
    
def draw_canvas(width, height, content, background_color="white"):
    svg_str = gen_canvas(width, height, content, background_color="white")
    return SVG(svg_str)
    
def svg_to_png(svg_str, png_file,w,h,upscale=1.0):
    # https://stackoverflow.com/questions/69660200/how-to-render-svg-image-to-png-file-in-python/69791039
    cairosvg.svg2png(bytestring=svg_str.encode(),write_to=png_file, 
        output_width=w*upscale, output_height=h*upscale)

def svg_to_png_data(svg_str,w,h,upscale=1.0):
    # https://stackoverflow.com/questions/69660200/how-to-render-svg-image-to-png-file-in-python/69791039
    png_bytes = cairosvg.svg2png(bytestring=svg_str.encode(), 
        output_width=w*upscale, output_height=h*upscale)
    return Image.open(io.BytesIO(png_bytes)).convert('RGBA')

#%%
# SHAPES
def circle(cx, cy, r, fill="white", stroke_width=5, stroke="black"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke-width="{stroke_width}" stroke="{stroke}"></circle>'
    
def triangle(x1,y1, x2,y2, x3,y3, fill="white", stroke_width=0, stroke="black"):
    return f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" fill="{fill}" stroke-width="{stroke_width}" stroke="{stroke}" class="triangle" />'
    # return f''

def bezier(p1, c1, c2, p2, stroke_width=5, stroke="black", fill="transparent"):
    return f'<path d="M {p1[0]} {p1[1]} C {c1[0]} {c1[1]}, {c2[0]} {c2[1]}, {p2[0]} {p2[1]}" stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"/>'
    #REF: https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
    
# PATHS 
def line(x1,y1, x2,y2, stroke_width=3, stroke="black"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="{stroke_width}" stroke="{stroke}"/>'

def text(content, x=w, y=h, fontsize="45px", font_weight="normal", font="monospace", fill='black'):
    return f'<text x="{x}" y="{y}" font-size="{fontsize}" font-family="{font}" fill="{fill}" text-anchor="middle" dominant-baseline="middle">{content}</text>'

# TRANSFORMS
def translate(shape, tx=w,ty=h):
    return f'<g transform="translate({tx},{ty})">'+shape+'</g>'
    
def rotate(shape, ang, rx, ry):
    return f'<g transform="rotate({ang} {rx} {ry})">'+shape+'</g>'
def scale(shape, sx=1.0,sy=None):
    if sy is None:
        sy = sx
    return f'<g transform="scale({sx} {sy})">'+shape+'</g>'

#%% 
# Utilities, higher order plotting
def get_angle(xy):
    return np.arctan2(xy[0],xy[1])
def get_mag(xy):
    return np.sqrt(xy[0]**2 + xy[1]**2)
    
def draw_arrow(start, end=None, diff=None,r_back=0,displace_x=0,
    color='black',stroke_width=3,
    ahw=10):
    if diff is None:
        diff = np.array(end)-np.array(start)
    if end is None:
        end = np.array(start)+np.array(diff)
    s = ''
    
    y_arrow = get_mag(diff)-r_back
    # ahw = 10 # arrow_head_width

    #draw arrow body 
    s += line(0, y_arrow-ahw,0,0,stroke=color,stroke_width=stroke_width)
    #draw arrow head
    head = triangle(-ahw/2,-ahw,  ahw/2,-ahw, 0,0,fill=color,stroke=color)
    s += translate(head,0,y_arrow)
    
    s = translate(s,displace_x,0)
    s = rotate(s, -np.degrees(get_angle(diff)),0,0)
    s = translate(s,start[0],start[1])
    
    return s
#%%
# Network SVG plotting 
# consider moving this to network_plotting_functions
def nx_to_svg(G, node_size=20, scale=100, do_label=True, text_size=30, pos=None,
    node_edge_color = 'black',
    node_face_color = 'lightgrey',
    arrow_edge_color = 'black',
    arrow_width = 3,
    arrow_head_width = 9,
    arrow_displace_ratio = 1/3 , 
    arrow_node_spacing = 1.1, 
    ):
    '''
    node_face_color 
    node_edge_color 
    node_edge_width
    
    text_color
    text_size
    
    arrow_edge_color
    arrow_width
    arrow_head_width
    arrow_displace_ratio = 1/3
    '''    
    '''
    for minimal glyphs 
    node_size=8,do_label=False,
    arrow_head_width=20,
    arrow_width=6,
    arrow_displace_ratio = 0.7,
    node_face_color='black',
    
    '''
    node_edge_width = 3

    text_color = 'black'
    

    
    #relative to node size
    
    svg_str = ''
    if pos is None:
        pos = netplot.clockwise_circular_layout(G)
    
    def pos_to_coord(pos_i):
        x,y = np.array(pos_i)*scale
        y *= -1
        return np.array([x,y])
    
    # draw edges
    for e in G.edges():
        xyS = pos_to_coord(pos[e[0]])
        xyT = pos_to_coord(pos[e[1]])
        
        disp_x = 0
        # if edge is bidirectional, displace it
        if G.has_edge(e[1],e[0]):
            disp_x = node_size*arrow_displace_ratio
        
        # draw arrow    
        svg_str += draw_arrow(xyS,xyT, 
            r_back=node_size*arrow_node_spacing, displace_x = disp_x,
            color=arrow_edge_color, stroke_width=arrow_width,
            ahw=arrow_head_width)
    
    # draw nodes
    for n in sorted(G.nodes()):
        x,y = pos_to_coord(pos[n])
        svg_str += circle(x,y,r=node_size,
            stroke_width=node_edge_width,stroke=node_edge_color,fill=node_face_color)
            
        if do_label:
            svg_str += text(str(n),x,y,fontsize=f'{text_size}px',fill=text_color)
    
    # svg_str = svg.scale(svg_str,1)
    return svg_str 

def nx_to_svg_img(G, node_size=20, scale=100, do_label=True, text_size=40, pos=None,
        node_edge_color = 'black',
        node_face_color = 'lightgrey',
        arrow_edge_color = 'black',
        arrow_width = 3,
        arrow_head_width = 9,
        arrow_displace_ratio = 1/3 , 
        arrow_node_spacing = 1.1, 
        border_padding=0.1,W=None,H=None,
        save_png_file=None,png_scale=5):
        
    if W is None:
        W = 2.5*scale*(1+border_padding)
    if H is None:
        H = W
    
    nx_svg = nx_to_svg(G, node_size=node_size, scale=scale, do_label=do_label, text_size=text_size, pos=pos,
        node_face_color=node_face_color,
        node_edge_color = node_edge_color,
        arrow_edge_color = arrow_edge_color,
        arrow_width = arrow_width,
        arrow_head_width = arrow_head_width,
        arrow_displace_ratio = arrow_displace_ratio, 
        arrow_node_spacing = arrow_node_spacing) 
        
    svg_placed = translate(nx_svg,W/2,H/2)
    svg_img = gen_canvas(W,H,svg_placed)
    
    if save_png_file:
        svg_to_png(svg_img,save_png_file,W,H,upscale=5)
    svg_png = svg_to_png_data(svg_img,W,H,upscale=5)
    return svg_img, svg_png
#%%
if __name__ == "__main__":
    import _svg_draw as svg
    import matplotlib.pyplot as plt 
    import networkx as nx 

    import network_plotting_functions as netplot
    import numpy as np
    #canvas 
    W = 250 
    H = W
    w = W/2
    h = H/2
    #%%    
    G = nx.DiGraph({0:[1],1:[2]})
    G = nx.DiGraph({'1':['5'],'2':['3'],'3':['2'],'4':['1'],'5':['2','3','4'],'6':['2']})
    G = netplot.relabel_nodes_abc(G)

    #%%
    #generate svg, save to png file
    # return svg encoded, png image data
    svg_img, svg_png = svg.nx_to_svg_img(G, save_png_file='tmp.png')
    #render SVG in notebook
    svg.SVG(svg_img)
    #%%
    # can either read in image from file
    fig,ax = plt.subplots(2,2,figsize=(5,5))
    img = plt.imread('tmp.png')
    ax[0][0].imshow(img)
    # or use svg png data without file
    ax[1][1].imshow(svg_png)
    fig