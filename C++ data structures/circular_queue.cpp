#include<iostream>

using namespace std;

#define SIZE 10

class CircularQueue
{
    int a[SIZE];
    int rear;   //same as tail
    int front;  //same as head
  
    public:
    CircularQueue()
    {
        rear = front = -1;
    }
    
    // function to check if queue is full
    bool isFull()
    {
        if(front == 0 && rear == SIZE - 1)
        {
            return true;
        }
        if(front == rear + 1) 
        {
            return true;
        }
        return false;
    }
    
    // function to check if queue is empty
    bool isEmpty()
    {
        if(front == -1) 
        {
            return true;
        }
        else 
        {
            return false;
        }
    }
    
    //declaring enqueue, dequeue, display and size functions
    void enqueue(int x);     
    int dequeue();
    void display();
};

// function enqueue - to add data to queue
void CircularQueue :: enqueue(int x)
{
    if(isFull())
    {
        cout << "Queue is full";
    } 
    else 
    {
        if(front == -1)
        {   
            front = 0;
        }
        rear = (rear + 1) % SIZE;   // going round and round concept
        // inserting the element
        a[rear] = x;
        cout << endl << "Inserted " << x << endl;
    }
}

// function dequeue - to remove data from queue
int CircularQueue :: dequeue()
{
    int y;
    
    if(isEmpty())
    {
        cout << "Queue is empty" << endl;
    } 
    else 
    {
        y = a[front];
        if(front == rear)
        {
            // only one element in queue, reset queue after removal
            front = -1;
            rear = -1;
        }
        else 
        {
            front = (front+1) % SIZE;
        }
        return(y);
    }
}

void CircularQueue :: display()
{
    /* Function to display status of Circular Queue */
    int i;
    if(isEmpty()) 
    {
        cout << endl << "Empty Queue" << endl;
    }
    else
    {
        cout << endl << "Front -> " << front;
        cout << endl << "Elements -> ";
        for(i = front; i != rear; i= (i+1) % SIZE)
        {
            cout << a[i] << "\t";
        }
        cout << a[i];
        cout << endl << "Rear -> " << rear;
    }
}



// the main function
int main()
{
    int ch,item;
    CircularQueue cq;
    cout<<"choice:\n1.Enqueue\n2.Dequeue\n3.Display\nexit\n";
    do{
        cout<<"\nEnter your choice:"<<endl;
        cin>>ch;
        switch(ch)
        {
            case 1: cout<<"Enter the item:"<<endl;
                    cin>>item;
                    cq.enqueue(item);
                    break;
            case 2: cout<<"Removed element is:"<<cq.dequeue();
                    break;
            case 3: cq.display();
                    break;
            case 4: exit(0);
                    break;
            default: cout<<"Invalid Input!"<<endl;
        }
    }while(1);
   
    
    
    return 0;
}

