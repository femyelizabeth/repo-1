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

Set Serveroutput ON
DECLARE
n number(5);
f number(2);
i number(5);
BEGIN
n:=&n;
f:=1;
for i in 1..n
loop
f:=f*i;
end loop;
dbms_output.Put_line('Factorial of '||n||' is: '||f);
end;
/
