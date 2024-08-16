function db_value = helper_linear_to_dB(x)
    db_value = 20 * log10(abs(x));
end