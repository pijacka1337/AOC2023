#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

void printVV(vector<vector<int>> &inputs){
    for(int i = 0; i < inputs.size(); i++){
        for(int j = 0; j < inputs[i].size(); j++){
            cout << inputs[i][j] << " ";
        }
        cout << endl;
    }
}

void printV(vector<int> &v){
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
}

int nextNumber (vector<int> &v){
    //printV(v);
    vector<int> diff;
    bool end = true;
    for(int i = 0; i < v.size() - 1; i++){
        int d = v[i+1] - v[i];
        if(d != 0){
            end = false;
        }
        diff.push_back(d);
    }
    if(end){
        return v[0];
    }
    else{
        //cout << "tu sem" << endl;
        //cout << "diff: ";
        //printV(diff);
        return v[v.size() - 1] + nextNumber(diff);
    }
}

int main()
{
    vector<vector<int>> inputs;
    string line;
    long long int sum = 0;

    ifstream inputFile("in.txt");
    cin.rdbuf(inputFile.rdbuf());

    while(getline(cin, line)){
        istringstream iss(line);
        vector<int> input;
        int num;
        while(iss >> num){
            input.push_back(num);
        }
        inputs.push_back(input);
    }

    //printVV(inputs);

    for(int i = 0; i < inputs.size(); i++){
        sum += nextNumber(inputs[i]);
        //cout<<"---------------------" << endl;
    }

    cout << sum << endl;

    

    return 0;
}
