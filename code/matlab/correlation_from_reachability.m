function r2 = correlation_from_reachability(i,j,Wt,s)
% NOTE: currently this uses Wt(to, from) indexing convention
    Wi = Wt(i,:);
    Wj = Wt(j,:);
    s_ = s.';
    
    r2_numer = sum( Wi.*Wj.*s_ );
    r2_denom = sqrt( sum(Wi.^2 .* s_) * sum(Wj.^2 .* s_) );
    r2 = r2_numer/r2_denom;
end