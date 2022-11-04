#include<iostream>
using namespace std;
int main()
{
    int quantity, choice;
    int Quantity_room=0, Quantity_pasta=0, Quantity_burger=0, Quantity_noodles=0, Quantity_shake=0, Quantity_chicken=0;
    int Sold_room=0, Sold_pasta=0, Sold_burger=0, Sold_noodles=0, Sold_shake=0, Sold_chicken=0;
    int Total_room=0, Total_pasta=0, Total_burger=0, Total_noodles=0, Total_shake=0, Total_chicken=0;
    
    cout<<"Quantity of items we have: ";
    cout<<"\nRooms available: ";
    cin>>Quantity_room;
    cout<<"\nQuantity of pasta: ";
    cin>>Quantity_pasta;
    cout<<"\nQuantity of burger: ";
    cin>>Quantity_burger;
    cout<<"\nQuantity of noodles: ";
    cin>>Quantity_noodles;
    cout<<"\nQuantity of shake: ";
    cin>>Quantity_shake;
    cout<<"\nQuantity of chicken roll: ";
    cin>>Quantity_chicken;

    cout<<"\n\nPlease select from the menu option";
    cout<<"\n1) Rooms\n2) Pasta\n3) Burger\n4) Noodles\n5) Shake\n6) Chicken roll\n7) Information regarding sales and collection\n8) Exit";
    cout<<"\nPlease enter your choice: ";
    cin>>choice;

    switch (choice)
    {
    case 1:
        cout<<"Enter the number of rooms you want: ";
        cin>>quantity;
        if(Quantity_room - Sold_room >= quantity)
        {
            Sold_room += quantity;
            Total_room += quantity * 1200;
            cout<<"\n"<<quantity<<" room/rooms have been alloted to you!";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_room - Sold_room<<" rooms are remaining in hotel.";
        }
        break;
    case 2:
        cout<<"Enter pasta quantity: ";
        cin>>quantity;
        if(Quantity_pasta - Sold_pasta >= quantity)
        {
            Sold_pasta += quantity;
            Total_pasta += quantity * 50;
            cout<<"\n"<<quantity<<" plates of pasta ordered.";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_pasta - Sold_pasta<<" plates of pasta are remaining in hotel.";
        }
        break;
    case 3:
        cout<<"Enter burger quantity: ";
        cin>>quantity;
        if(Quantity_burger - Sold_burger >= quantity)
        {
            Sold_burger += quantity;
            Total_burger += quantity * 50;
            cout<<"\n"<<quantity<<" plates of burger ordered.";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_burger - Sold_burger<<" plates of burger are remaining in hotel.";
        }
        break;
    case 4:
        cout<<"Enter noodles quantity: ";
        cin>>quantity;
        if(Quantity_noodles - Sold_noodles >= quantity)
        {
            Sold_noodles += quantity;
            Total_noodles += quantity * 50;
            cout<<"\n"<<quantity<<" plates of noodles ordered.";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_noodles - Sold_noodles<<" plates of noodles are remaining in hotel.";
        }
        break;
    case 5:
        cout<<"Enter shake quantity: ";
        cin>>quantity;
        if(Quantity_shake - Sold_shake >= quantity)
        {
            Sold_shake += quantity;
            Total_shake += quantity * 50;
            cout<<"\n"<<quantity<<" plates of shake ordered.";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_shake - Sold_shake<<" plates of shake are remaining in hotel.";
        }
        break;
    case 6:
        cout<<"Enter chicken roll quantity: ";
        cin>>quantity;
        if(Quantity_chicken - Sold_chicken >= quantity)
        {
            Sold_chicken += quantity;
            Total_chicken += quantity * 50;
            cout<<"\n"<<quantity<<" plates of chicken ordered.";
        }
        else
        {
            cout<<"\nOnly "<<Quantity_chicken - Sold_chicken<<" plates of chicken roll are remaining in hotel.";
        }
        break;
    default:
        break;
    }
}
