#include<iostream>
#include <time.h>
#include <vector>
using namespace std;

bool lose = false;
bool killedogre = false;
bool killedgoblin = false;
bool killedshop = false;
bool openedchest = false;
int room = 1;
int gold = 1000000;
int hp = 25;
string input = "i like trains";
string enemy = "default enemy";
int randnum = 0;

bool check(string thing);
void combat(int mobhp, int mobatk, int hp, string enemy);



vector<string> inv;


//inv.push_back("string")



int main() {
	srand(time(NULL)); //rand()%10+1
	while (lose == false) {
		if (room == 1) {
			cout << "you are in a strange clearing. There are paths leading, North, East, South, or West" << endl;
			cout << "what do you do" << endl;
			cin >> input;
			if (input == "south" || input == "s")
				room = 4;
			if (input == "north" || input == "n")
				room = 3;
			if (input == "east" || input == "e")
				room = 7;
			if (input == "west" || input == "w")
				room = 2;
			if (input == "g")
				combat(20, 5, hp, "default enemy");
			if (input == "gold")
				cout << gold << endl;
			if (input == "add")
				inv.push_back("test");
		}
		if (room == 2) {
			if (killedshop == false)
				cout << "A lone shop stands here. The shopkeep looks rather weak and frail. You can shop here or go East" << endl;
			if (killedshop == true) 
				cout << "the ruins of a small shop stand here. You can head back east." << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (input == "east" || input == "e")
					room = 1;
				if (input == "shop") {
					cout << "I can sell you these wonderful fireproof boots for 100 gold, this new set of armor for 50 gold, and this old, rusty sword for 150 gold." << endl;
					cin >> input;
					if (input == "boots") {
						if (gold >= 100) {
							cout << "enjoy these new boots" << endl;
							gold -= 100;
							//add boots to inv
						}
						if (gold < 100)
							cout << "you are too poor" << endl;
					}
					if (input == "armor") {
						if (gold >= 50) {
							cout << "enjoy this new armor" << endl;
							gold -= 50;
							//add armor to inv
						}
						if (gold < 50)
							cout << "you are too broke to shop here" << endl;
					}
					if (input == "sword") {
						if (gold >= 150) {
							cout << " enjoy!" << endl;
							gold -= 150;
							inv.push_back("rustysword");
						}
						if (gold < 150)
							cout << "you dont have enough money for that" << endl;
					}

				}
				if (input == "fight" || input == "steal" || input == "rob")
					combat(10, 1, hp, "angery shopkeep");


			}
			if (room == 3) {
				cout << "A strange orb lies in the middle of a clearin. Enemies occasinally spawn from it. You can fight them here or go South." << endl;
				cin >> input;
				if (input == "south" || input == "s")
					room = 1;
				if (input == "gold")
					cout << gold << endl;

			}
			if (room == 4) {
				cout << "An empty clearing. You can rest here, head North, or go South." << endl;
				cin >> input;
				if (input == "south" || input == "s")
					room = 5;
				if (input == "north" || input == "n")
					room = 1;
				if (input == "gold")
					cout << gold << endl;
			}
			if (room == 5) {
				if (killedogre == false)
					cout << "A large ogre has been alerted to your pressance! You must fight it here or retreat North." << endl;
				if (killedogre == true)
					cout << "You enter the empty cave the large ogre once occupied. You can head North." << endl;
				cin >> input;
				if (input == "north" || input == "n")
					room = 4;
				if (input == "fight" && killedogre == false)
					combat(25, 4, hp, "ogre");
				if (input == "gold")
					cout << gold << endl;
			}
			if (room == 7) {
				if (killedgoblin == false)
					cout << "A small goblin stops you. Fight him to continue North or East, or head pack West." << endl;
				if (killedgoblin == true)
					cout << "An empty path. You can head North, East, or West" << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (killedgoblin == false) {
					if (input == "north" || input == "n")
						room = 6;
					if (input == "east" || input == "e")
						room = 8;
				}
				if (input == "west" || input == "w")
					room = 1;
				if (input == "fight" || input == "steal" || input == "rob")
					combat(10, 2, hp, "small goblin");
			}
			if (room == 6) {
				cout << "A slots machine sits in a small shack. You can spin it or head back South." << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (input == "south" || input == "s")
					room = 7;
			}
			if (room == 8) {
				if(openedchest == false)
					cout << "A chest lies in the middle of the path. You are sure it is not a mimic. Open it, continue East or head back West." << endl;
				if (openedchest == true)
					cout << "an empty path. Can go East or West" << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (input == "east" || input == "e")
					room = 9;
				if (input == "west" || input == "w")
					room = 7;
				if (input == "open"){
					cout << "you opened the chest and gained 117 gold!" << endl;
				gold += 117;
			}
			}
			if (room == 9) {
				cout << "The ground in the path is glowing red and radaiting heat. To continue North you must find a way to protect your feet. That or head back the way you came (west)" << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (input == "north" || input == "n")
					room = 10;
				if (input == "west" || input == "w")
					room = 8;
			}
			if (room == 10) {
				cout << "Krumblor, the Cookie Dragon is chained down in a large clearing. The chains all have the same lock. One key should be all it takes to free him. The only exit is to the south, unless you free Krumblor." << endl;
				cin >> input;
				if (input == "gold")
					cout << gold << endl;
				if (input == "south" || input == "s")
					room = 9;
			}
			//end loop
		}
		//end main
	}

//combat function
void combat(int mobhp, int mobatk, int hp, string enemy) {
	cout << enemy << " attacks, stats are " << mobhp << " hp and " << mobatk << " attack" << endl;
	bool fight = true;
	int atk = 3;
	if (check("test") == true) 
		atk = 8;
	if (check("rustysword") == true)
		atk = 12;
	while (fight == true) {
		if (mobhp <= 0) {
			cout << enemy << " has been defeated!" << endl;
			fight = false;
			if (enemy == "ogre") {
				cout << "Obtained 100 gold and key!" << endl;
				killedogre = true;
				gold += 100;
				//add key to inv 
			}
			if (enemy == "goblin") {
				killedgoblin = true;
				gold += 7;
				cout << "Obtained 7 gold!" << endl;
			}
			if (enemy == "angery shopkeep") {
				cout << "Enjoy his items at least." << endl;
				cout << "obtained, 57 gold, Rusty Sword, Armor, and Fire Proof Boots!" << endl;
				killedshop = true;
				gold += 57;
				//add armor to inv
				//add sword to inv
				//add boots to inv
			}
		}

		if (hp <= 0) {
			cout << "You died!" << endl;
			fight = false;
			lose = true;
		}
		if (fight == true) {
			cout << "do you attack or run?" << endl;
			cin >> input;
			if (input == "run" || input == "r") {
				cout << "you attemp to escape" << endl;
				randnum = rand() % 10 + 1;
				if (randnum < 5) {
					cout << "you got away" << endl;
					room = 1;
					fight = false;
				}
				else {
					cout << "you did not escape" << endl;
				}
			}
			if (input == "fight" || input == "attack" || input == "atk") {
				randnum = rand() % 10 + 1;
				if (randnum == 1)
					cout << "you missed, idiot" << endl;
				else {
					mobhp -= atk;
					cout << "hit " << enemy << " for " << atk << " damage! It has " << mobhp << " left." << endl;
				}
			}
			hp -= mobatk;
			cout << enemy << " hit you! You took " << mobatk << " damage! You have " << hp << " left." << endl;
		}
		//end loop
	}
	//end function
}


bool check(string thing) {
	for (int x = 0; x<inv.size(); x++) {
		if (inv[x] == thing) {
			return true;
		}
	}
	return false;


}