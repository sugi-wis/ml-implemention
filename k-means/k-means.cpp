#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <cmath>
#include <fstream>

const int K = 6;
const int pNum = 100;
const int ItrNum = 10;
typedef std::vector<std::vector<float>> position; 

class Point{
	public:
	float pos[2]={};
	int mData;
};
class Mean{
	public:
	float pos[2]={};
};

void CalcMeansData(std::vector<Point> &p,std::vector<Mean> &m);

int main()
{
	using namespace std;

	clock_t start,end;
	start = clock();
	
	vector<Point> p(pNum);
	vector<Mean> m(K);

	random_device rnd;
	mt19937 mt(rnd());
	//uniform_int_distribution<int> rndInt(0,10);
	uniform_real_distribution<float> rndF(0,100);
	
	
	position means(K,vector<float>(2));
	position points(pNum,vector<float>(2));
	vector<int> pData(pNum);

	for (int i=0;i<K;i++){
		m[i].pos[0] = rndF(mt);
		m[i].pos[1] = rndF(mt);
	}
	for(int i=0;i<pNum;i++){
		p[i].pos[0]= rndF(mt);
		p[i].pos[1]= rndF(mt);
	}	
	for (int i=0;i<K;i++){
		means.at(i).at(0) = rndF(mt);
		means[i][1] = rndF(mt);
	}
	for(int i=0;i<pNum;i++){
		points[i][0]= rndF(mt);
		points[i][1]= rndF(mt);
	}
	/*
	for (int i=0;i<pNum;i++){
		
		int minMeanNum = -1;
		float minDtc = -1;
		for (int k = 0;k < K;k++){
			float dtc = pow(points[i][0] - means[k][0],2)
			+ pow(points[i][1] - means[k][1],2);
			if(minDtc < 0 || minDtc > dtc)
			{minDtc = dtc;minMeanNum = k;}
		}
		pData[i] = minMeanNum;
	}
	*/
	
	CalcMeansData(p,m);

	ofstream ofs("data.csv");
	for(int k = 0;k<K;k++){
		ofs << means[k][0] << " "<< means[k][1]
		<<" "<< k << endl;
	}
	for(int i=0;i<pNum;i++){
		ofs << points[i][0] << " "<< points[i][1]
		<<" "<< pData[i] << endl;
	}
	
	end = clock();
	cout << (double)(end-start)/CLOCKS_PER_SEC << endl;
	
}

void CalcMeansData(std::vector<Point> &p,std::vector<Mean> &m)
{
	
	for (int i=0;i<pNum;i++){
		
		int minMeanNum = -1;
		
		float minDtc = -1;
		for (int k = 0;k < K;k++){
			float dtc = pow(p[i].pos[0] - m[k].pos[0],2)
			+ pow(p[i].pos[1] - m[k].pos[1],2);
			if(minDtc < 0 || minDtc > dtc)
			{minDtc = dtc;minMeanNum = k;}
		}
		  p[i].mData = minMeanNum;
	}
}

void SetMeansData()
{
}
