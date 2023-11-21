package com.example.login_form1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText usernameE;
    private EditText passwordE;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        usernameE=findViewById(R.id.usernameE);
        passwordE=findViewById(R.id.passwordE);
    }

    public void login(View view){
        String username = usernameE.getText().toString();
        String password = passwordE.getText().toString();

        if (!username.isEmpty() && !password.isEmpty()){

            Toast.makeText(this, "Login successful", Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this, "Invalid credentials", Toast.LENGTH_SHORT).show();
        }
    }
}
