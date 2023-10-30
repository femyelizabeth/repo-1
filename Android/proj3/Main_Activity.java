//MainActivity.java
package com.example.femyapp4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.view.Gravity;
import android.graphics.Color;
import android.graphics.Typeface;

public class MainActivity extends AppCompatActivity {
    LinearLayout l1;
    TextView t;
    Button b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        l1=new LinearLayout(this);
        t=new TextView(this);
        t.setText("Hello All!");
        t.setGravity(Gravity.CENTER);
        t.setTextSize(35);
        t.setTextColor(Color.BLUE);
        t.setTypeface(Typeface.DEFAULT_BOLD);

        b=new Button(this);
        b.setText("Hi Button");
        b.setBackgroundColor(Color.CYAN);

        LinearLayout.LayoutParams vdim=new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,ViewGroup.LayoutParams.WRAP_CONTENT);
        vdim.setMargins(0,50,0,0);
        t.setLayoutParams(vdim);
        b.setLayoutParams(vdim);

        l1.setOrientation(LinearLayout.VERTICAL);
        l1.setGravity(Gravity.CENTER);

        l1.addView(t);
        l1.addView(b);

        setContentView(l1);


    }
}
