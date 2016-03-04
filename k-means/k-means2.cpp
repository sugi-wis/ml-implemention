#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <cmath>
#include <fstream>

const int K = 6;
const int pNum = 100;
const int ItrNum = 5;
typedef std::vector<std::vector<float>> position; 

using std::cout;using std::endl;using std::string;
class Point{
	public:
	float pos[2]={};
	int mData;
	void SetPos(float x,float y)
	{
		pos[0] = x;pos[1] = y;
	}
};
class Mean{
	public:
	float pos[2]={};
	void SetPos(float x,float y)
	{
		pos[0] = x;pos[1] = y;
	}
};


void CalcMeansData(std::vector<Point> &p,std::vector<Mean> &m);
void WriteData(std::vector<Point> &p,std::vector<Mean> &m,string name);
void ResetMpos(std::vector<Point> &p,std::vector<Mean> &m);

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

	for (int i=0;i<K;i++) m[i].SetPos(rndF(mt),rndF(mt));
	for (int i=0;i<pNum;i++) p[i].SetPos(rndF(mt),rndF(mt));
	
	CalcMeansData(p,m);
	WriteData(p,m,"FirstState");
	for(int i=0;i<ItrNum;i++){
		CalcMeansData(p,m);		//calc and set mean data of points
		ResetMpos(p,m);			//reset means' position
	}
	WriteData(p,m,"AfterProcess");


	end = clock();
	cout <<"process time " << (double)(end-start)/CLOCKS_PER_SEC << endl;
	
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
void WriteData(std::vector<Point> &p,std::vector<Mean> &m,string name)
{
	std::ofstream ofs(name + ".csv");
	for(int k = 0;k<K;k++){
		ofs << m[k].pos[0] << " "<< m[k].pos[1]
		<<" "<< k << endl;
		cout << m[k].pos[0] << " "<< m[k].pos[1]
		<<" "<< k << endl;
	}
	for(int i=0;i<pNum;i++){
		ofs << p[i].pos[0] << " "<< p[i].pos[1]
		<<" "<< p[i].mData << endl;
	}	
}

void ResetMpos(std::vector<Point> &p,std::vector<Mean> &m)
{
	for(int k=0;k<K;k++){
		float x=0,y =0;
		int cnt = 0;
		for(int i=0;i<pNum;i++){
			if(k == p[i].mData){
				x += p[i].pos[0];
				y += p[i].pos[1];
				cnt++;
			}
		}
		if(cnt != 0) m[k].SetPos(x/cnt,y/cnt);
	}
}
