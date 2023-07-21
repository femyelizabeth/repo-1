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
