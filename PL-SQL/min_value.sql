
set serveroutput On
Declare
    value number;
procedure find_min(a in number, b in number, min out number) is 
BEGIN
    if a < b then
        min := a;
    else
        min := b;
    end if;
end;

BEGIN
    find_min(10, 5, value);
    dbms_output.put_line('Minimum value is: ' || value);
end;
/
