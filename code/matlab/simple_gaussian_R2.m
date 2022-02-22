% parameters

param_vals = linspace(0,5,100);
n = 100000;

r2_vals = zeros(size(param_vals));
r2_emp_vals = zeros(size(param_vals));
%%
for param_i = 1:numel(param_vals)
  fprintf('Computing trial %d/%d...', param_i, numel(param_vals));
  param_val = param_vals(param_i);
  
  % set parameter values
  
  exog_var_a = 1;
  exog_var_b = 1;
  exog_var_sa = 1;
  exog_var_sb = 1;
  exog_var_sz = 1;

  w_sa_a = 1;
  w_sz_a = 1;
  w_sz_b = param_val;
  w_sb_b = 1;
  w_a_b = 1;

  % construct linear-algebraic form
  W = [0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    w_sa_a, 0, w_sz_a, 0, 0;
    0, w_sb_b, w_sz_b, w_a_b, 0];
  s = [exog_var_sa;
    exog_var_sb;
    exog_var_sz;
    exog_var_a;
    exog_var_b];

  Wt = zeros(length(s));
  for i = 0:length(s)
    Wt = Wt + W^i;
  end
  r2 = correlation_from_reachability(4,5,Wt,s)

  r2_vals(param_i) = r2;
  fprintf('done!\n');
  
  % empirically compute r2(a,b)
  
  e_sa = sqrt(exog_var_sa)*randn(1,n);
  e_sb = sqrt(exog_var_sb)*randn(1,n);
  e_sz = sqrt(exog_var_sz)*randn(1,n);
  e_a = sqrt(exog_var_a)*randn(1,n);
  e_b = sqrt(exog_var_b)*randn(1,n);
  
  sa = e_sa;
  sb = e_sb;
  sz = e_sz;
  a = w_sa_a*sa + w_sz_a*sz + e_a;
  b = w_sb_b*sb + w_sz_b*sz + w_a_b*a + e_b;
  r2_emp_vals(param_i) = corr(a.',b.');
  
end
%%
clf; plot(param_vals, r2_vals); hold on; plot(param_vals, r2_emp_vals,'--');
xlabel('w_{Sz->B}'); ylabel('r^2(a,b)'); grid on; ylim([0 1]);
set(gca,'fontsize',16);
%%

