#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

// MenuItem structure
struct MenuItem {
    char name[30];
    float price;
};

// Static menu array (starts empty)
static MenuItem menu[20] = {};
static int menuSize = 0;

// Abstract Order class
class Order {
protected:
    MenuItem** items;
    int nItems;
    int capacity;
    static int nextOrderId;
    int orderId;

public:
    Order() : items(nullptr), nItems(0), capacity(0) {
        orderId = ++nextOrderId;
        items = new MenuItem*[10];
        capacity = 10;
    }

    virtual ~Order() {
        delete[] items;
    }

    void addItem(MenuItem* item) {
        if (nItems >= capacity) {
            MenuItem** newItems = new MenuItem*[capacity * 2];
            for (int i = 0; i < nItems; i++) {
                newItems[i] = items[i];
            }
            delete[] items;
            items = newItems;
            capacity *= 2;
        }
        items[nItems++] = item;
    }

    float getItemsTotal() const {
        float total = 0.0f;
        MenuItem** ptr = items;
        for (int i = 0; i < nItems; i++) {
            total += (*(ptr + i))->price;
        }
        return total;
    }

    virtual float getTotal() const = 0;

    int getOrderId() const { return orderId; }
    int getItemCount() const { return nItems; }

    void displayItems() const {
        cout << "Order #" << orderId << " items:\n";
        for (int i = 0; i < nItems; i++) {
            cout << "  - " << items[i]->name << " ($" << fixed << setprecision(2) << items[i]->price << ")\n";
        }
    }
};

int Order::nextOrderId = 0;

// DineInOrder class
class DineInOrder : public Order {
private:
    float serviceFee;

public:
    DineInOrder(float fee = 2.50f) : Order(), serviceFee(fee) {}

    float getTotal() const override {
        return getItemsTotal() + serviceFee;
    }

    void displayOrder() const {
        displayItems();
        cout << "  Service Fee: $" << fixed << setprecision(2) << serviceFee << "\n";
        cout << "  Total: $" << fixed << setprecision(2) << getTotal() << "\n";
        cout << "  Type: Dine-In\n\n";
    }
};

// CarryOutOrder class
class CarryOutOrder : public Order {
private:
    float packagingFee;

public:
    CarryOutOrder(float fee = 1.00f) : Order(), packagingFee(fee) {}

    float getTotal() const override {
        return getItemsTotal() + packagingFee;
    }

    void displayOrder() const {
        displayItems();
        cout << "  Packaging Fee: $" << fixed << setprecision(2) << packagingFee << "\n";
        cout << "  Total: $" << fixed << setprecision(2) << getTotal() << "\n";
        cout << "  Type: Carry-Out\n\n";
    }
};

// Order Manager
class RestaurantOrderManager {
private:
    Order** orders;
    int nOrders;
    int capacity;

public:
    RestaurantOrderManager() : orders(nullptr), nOrders(0), capacity(0) {
        orders = new Order*[10];
        capacity = 10;
    }

    ~RestaurantOrderManager() {
        for (int i = 0; i < nOrders; i++) {
            delete orders[i];
        }
        delete[] orders;
    }

    void addOrder(Order* order) {
        if (nOrders >= capacity) {
            Order** newOrders = new Order*[capacity * 2];
            for (int i = 0; i < nOrders; i++) {
                newOrders[i] = orders[i];
            }
            delete[] orders;
            orders = newOrders;
            capacity *= 2;
        }
        orders[nOrders++] = order;
    }

    bool removeOrder(int orderId) {
        for (int i = 0; i < nOrders; i++) {
            if (orders[i]->getOrderId() == orderId) {
                delete orders[i];
                for (int j = i; j < nOrders - 1; j++) {
                    orders[j] = orders[j + 1];
                }
                nOrders--;
                if (nOrders < capacity / 4 && capacity > 10) {
                    Order** newOrders = new Order*[capacity / 2];
                    for (int k = 0; k < nOrders; k++) {
                        newOrders[k] = orders[k];
                    }
                    delete[] orders;
                    orders = newOrders;
                    capacity /= 2;
                }
                return true;
            }
        }
        return false;
    }

    void displayAllOrders() const {
        if (nOrders == 0) {
            cout << "No orders found.\n\n";
            return;
        }

        cout << "\n=== ALL ORDERS ===\n";
        for (int i = 0; i < nOrders; i++) {
            cout << "Order #" << orders[i]->getOrderId()
                 << " - Total: $" << fixed << setprecision(2) << orders[i]->getTotal();

            DineInOrder* dineIn = dynamic_cast<DineInOrder*>(orders[i]);
            CarryOutOrder* carryOut = dynamic_cast<CarryOutOrder*>(orders[i]);

            if (dineIn) {
                cout << " (Dine-In)\n";
                dineIn->displayOrder();
            } else if (carryOut) {
                cout << " (Carry-Out)\n";
                carryOut->displayOrder();
            }
        }
    }

    float getTotalRevenue() const {
        float total = 0.0f;
        for (int i = 0; i < nOrders; i++) {
            total += orders[i]->getTotal();
        }
        return total;
    }

    int getOrderCount() const { return nOrders; }
};

// Utility Functions
void displayMenu() {
    cout << "\n=== MENU ===\n";
    if (menuSize == 0) {
        cout << "Menu is currently empty.\n\n";
        return;
    }
    for (int i = 0; i < menuSize; i++) {
        cout << (i + 1) << ". " << menu[i].name
             << " - $" << fixed << setprecision(2) << menu[i].price << "\n";
    }
    cout << "\n";
}

int getValidChoice(int min, int max) {
    int choice;
    while (true) {
        cout << "Enter choice (" << min << "-" << max << "): ";
        cin >> choice;
        if (cin.fail() || choice < min || choice > max) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Invalid choice. Please try again.\n";
        } else {
            cin.ignore(10000, '\n');
            return choice;
        }
    }
}

void addMenuItem() {
    if (menuSize >= 20) {
        cout << "Menu is full. Cannot add more items.\n";
        return;
    }

    MenuItem newItem;
    cout << "Enter item name: ";
    cin.ignore();
    cin.getline(newItem.name, 30);

    cout << "Enter item price: ";
    cin >> newItem.price;

    menu[menuSize++] = newItem;
    cout << "Item added to menu successfully!\n";
}

Order* createOrder() {
    if (menuSize == 0) {
        cout << "\nMenu is empty. Please add menu items before creating an order.\n";
        return nullptr;
    }

    cout << "\nSelect order type:\n";
    cout << "1. Dine-In Order (Service Fee: $2.50)\n";
    cout << "2. Carry-Out Order (Packaging Fee: $1.00)\n";

    int orderType = getValidChoice(1, 2);

    Order* order;
    if (orderType == 1) {
        order = new DineInOrder();
    } else {
        order = new CarryOutOrder();
    }

    cout << "\nAdding items to order...\n";
    while (true) {
        displayMenu();
        cout << "0. Finish adding items\n";

        int itemChoice = getValidChoice(0, menuSize);
        if (itemChoice == 0) break;

        order->addItem(&menu[itemChoice - 1]);
        cout << "Added " << menu[itemChoice - 1].name << " to order.\n";
    }

    return order;
}

void displayMainMenu() {
    cout << "\n=== RESTAURANT ORDER MANAGER ===\n";
    cout << "1. Add Menu Item\n";
    cout << "2. Create New Order\n";
    cout << "3. View All Orders\n";
    cout << "4. Remove Order\n";
    cout << "5. View Total Revenue\n";
    cout << "6. View Menu\n";
    cout << "7. Exit\n";
}

int main() {
    RestaurantOrderManager manager;

    cout << "Welcome to the Restaurant Order Manager!\n";

    while (true) {
        displayMainMenu();
        int choice = getValidChoice(1, 7);

        switch (choice) {
            case 1:
                addMenuItem();
                break;

            case 2: {
                Order* newOrder = createOrder();
                if (newOrder != nullptr) {
                    manager.addOrder(newOrder);
                    cout << "\nOrder #" << newOrder->getOrderId()
                         << " created successfully! Total: $"
                         << fixed << setprecision(2) << newOrder->getTotal() << "\n";
                }
                break;
            }

            case 3:
                manager.displayAllOrders();
                cout << "Enter Order ID to remove: ";
                int orderId;
                cin >> orderId;
                cin.ignore(10000, '\n');
                if (manager.removeOrder(orderId)) {
                    cout << "Order #" << orderId << " removed successfully.\n";
                } else {
                    cout << "Order #" << orderId << " not found.\n";
                }
                break;

            case 4:
                cout << "\nTotal Revenue: $" << fixed << setprecision(2)
                     << manager.getTotalRevenue() << "\n";
                cout << "Number of Orders: " << manager.getOrderCount() << "\n";
                break;

            case 5:
                displayMenu();
                break;

            case 6:
                displayMenu();
                break;

            case 7:
                cout << "Thank you for using Restaurant Order Manager!\n";
                return 0;
        }

        cout << "\nPress Enter to continue...";
        cin.get();
    }

    return 0;
}
