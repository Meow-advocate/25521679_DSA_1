#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <chrono>
#include <iomanip> 

using namespace std;
using namespace std::chrono;

double total_duration_ms = 0; 

void solve(string filename) {
    vector<double> data;
    double x;
    
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Khong the mo file: " << filename << endl;
        return;
    }

    while (file >> x) {
        data.push_back(x);
    }
    file.close();

    auto start = high_resolution_clock::now();
    sort(data.begin(), data.end());
    auto end = high_resolution_clock::now();
    
    auto duration = duration_cast<microseconds>(end - start);    
    double thoi_gian_ms = duration.count() / 1000.0;
    total_duration_ms += thoi_gian_ms;  
    cout << "File: " << filename << " | C++ Sort: " << fixed << setprecision(2) << thoi_gian_ms << " ms" << endl;
}

int main() {
    string files[] = {
        "thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"
    };

    for (const string& f : files) {
        solve(f);
    }
    cout << "Trung binh: " << fixed << setprecision(2) << total_duration_ms / 10.0 << " ms" << endl;    
    return 0;
}
