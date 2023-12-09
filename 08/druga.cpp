#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;


int main() {
    ifstream inputFile("in.txt");
    cin.rdbuf(inputFile.rdbuf());

    string directions;
    cin >> directions;

    cout << directions << " " << directions.size() << endl;

    string line;
    vector<pair<string, pair<string,string>>> nodesString;
    map<string, int> nodeMap;
    map<int, string> nodeMapReverse;
    vector<pair<int, pair<int,int>>> nodes;

    getline(cin, line); // skip empty line
    getline(cin, line);

    while (getline(cin, line)){
        //cout << line << endl;

        string s1 = "";
        string s2 = "";
        string s3 = "";

        int i = 0;
        while(line[i] != ' '){
            s1 += line[i];
            i++;
        }
        i += 4;
        while(line[i] != ','){
            s2 += line[i];
            i++;
        }
        i += 2;
        while(line[i] != ')'){
            s3 += line[i];
            i++;
        }

        cout << s1 << " " << s2 << " " << s3 << endl;

        nodesString.push_back(make_pair(s1, make_pair(s2, s3)));
        nodeMap[s1] = nodesString.size() - 1;
        nodeMapReverse[nodesString.size() - 1] = s1;


        
    }

    for(auto node : nodesString){
        nodes.push_back(make_pair(nodeMap[node.first], make_pair(nodeMap[node.second.first], nodeMap[node.second.second])));
    }

    for(auto node : nodes){
        cout << node.first << " " << node.second.first << " " << node.second.second << endl;
    }
    vector<int> startNodes;

    for(int num = 0; num < nodes.size(); num++){
        if(nodeMapReverse[num][2] == 'A'){
            startNodes.push_back(num);
        }
    }

    cout << "start nodes: ";
    for (auto x : startNodes){
        cout << x << " ";
    }
    cout << endl;

    vector<int> cycle_lengths;


    for(int k = 0; k < startNodes.size(); k++){
        int c = startNodes[k];
        int i = 0;
        int steps = 0;
        while(nodeMapReverse[c][2] != 'Z'){
            if(directions[i] == 'L'){
                c = nodes[c].second.first;
                steps ++;
                if(i != directions.size() -1){
                    i++;
                }
                else {
                    i = 0;
                }
                continue;
            }

            if(directions[i] == 'R'){
                c = nodes[c].second.second;
                steps ++;
                if(i != directions.size() -1){
                    i++;
                }
                else {
                    i = 0;
                }
                continue;
            }

        }
        cycle_lengths.push_back(steps);    
    }

    for(auto x : cycle_lengths){
        cout << x << " ";
    }
    long long int total_len = cycle_lengths[0];
    for(int i = 1; i < cycle_lengths.size(); i++){
        total_len = lcm(total_len, cycle_lengths[i]);
    }
    cout << total_len << endl;




    return 0;
}
