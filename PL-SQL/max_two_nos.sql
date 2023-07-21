function comp_max(a number, b number)
return NUMBER IS 
    max_value number;
BEGIN
    if a > b then
        max_value := a;
    else
        max_value := b;
    end if;

    return max_value;
end;

BEGIN
    result := comp_max(10,20);
    dbms_output.put_line('Maximum value is: ' || result);
end;
/

