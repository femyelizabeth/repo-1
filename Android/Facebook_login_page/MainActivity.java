package com.example.facebook_login;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText emailEditText = findViewById(R.id.editEmail);
        final EditText passwordEditText = findViewById(R.id.editPassword);
        final EditText confirmPasswordEditText = findViewById(R.id.editConfirmPassword);
        final CheckBox saveLoginCheckbox = findViewById(R.id.checkBoxSaveLogin);
        final CheckBox termsCheckbox = findViewById(R.id.checkBoxTerms);
        Button loginButton = findViewById(R.id.btnLogin);
        Button signUpBottom = findViewById(R.id.btnSignUp);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = emailEditText.getText().toString();
                String password = passwordEditText.getText().toString();

            }
        });

        signUpBottom.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = emailEditText.getText().toString();
                String password = passwordEditText.getText().toString();
                String confirmPassword = confirmPasswordEditText.getText().toString();

            }
        });
    }
}
