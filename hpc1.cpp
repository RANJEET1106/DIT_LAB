#include<bits/stdc++.h>
#include<omp.h>
using namespace std;

void bfs(vector<vector<int>>& g,int s){

    vector<int> vis(g.size(),0);
    queue<int> q;

    vis[s]=1;
    q.push(s);

    while(!q.empty()){

        int u=q.front();
        q.pop();

        cout<<u<<" ";

        #pragma omp parallel for
        for(int i=0;i<g[u].size();i++){

            int v=g[u][i];

            #pragma omp critical
            {
                if(!vis[v]){
                    vis[v]=1;
                    q.push(v);
                }
            }
        }
    }
}

void dfs(int u,vector<vector<int>>& g,vector<int>& vis){

    #pragma omp critical
    {
        if(vis[u]) return;
        vis[u]=1;
        cout<<u<<" ";
    }

    for(int v:g[u]){

        #pragma omp task
        dfs(v,g,vis);
    }
}

int main(){

    int n,e,u,v,s;
    cin>>n>>e;

    vector<vector<int>> g(n);

    while(e--){
        cin>>u>>v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    cin>>s;

    cout<<"BFS: ";
    bfs(g,s);

    vector<int> vis(n,0);

    cout<<"\nDFS: ";

    #pragma omp parallel
    {
        #pragma omp single
        dfs(s,g,vis);
    }
}