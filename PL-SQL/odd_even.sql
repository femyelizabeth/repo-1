
set Serveroutput On;
Declare
n number(4);
BEGIN
n:=&n;
if mod(n,2)=0 then
dbms_output.Put_line('number is even');
else
dbms_output.Put_line('number is odd');
end if;
end;
/
