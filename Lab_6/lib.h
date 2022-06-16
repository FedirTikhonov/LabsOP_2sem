#pragma once
#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

class ExpTree{
public:
    class TreeNode{
    public:
        TreeNode* left;
        TreeNode* right;
        TreeNode* parent;
        char value;
    };
    ExpTree() { root->right = nullptr; root->left = nullptr; root->parent = nullptr; };
    explicit ExpTree(const std::string& expression);
    TreeNode* root;
    void printSymmetrically(TreeNode* node, int lvl);
    void printDirectly(TreeNode* node, int lvl);
    void printPre(TreeNode* node);
    void printPost(TreeNode* node);
    void printIn(TreeNode* node);
};

bool isOperator(char c);
bool isNum(char c);
int precedence(char c);
std::string InfixToPrefix(std::stack<char> s, std::string infix);
void mainCode();