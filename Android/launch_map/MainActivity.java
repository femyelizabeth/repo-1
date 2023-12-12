package com.example.google_map;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    Intent intent, chooser=null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
     public void process(View v){
        if(v.getId()==R.id.btnShowMap)
        {
            intent = new Intent(intent.ACTION_VIEW);
            intent.setData(Uri.parse("geo:37.7749,-122.4194"));
            chooser = intent.createChooser(intent,"Show Map");
            startActivity(chooser);
        }
     }

}
