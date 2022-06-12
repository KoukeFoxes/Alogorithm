//implement queue using stack

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct node{
	int data;
	struct node *next;
};

struct node *top;

void push(int data){
	struct node *newnode;
	newnode = (struct node *)malloc(sizeof(struct node));
	newnode->data = data;
	newnode->next = top;
	top = newnode;
}

int pop(){
	struct node *temp;
	int data;
	if(top == NULL){
		printf("Underflow\n");
		return 0;
	}
	else{
		temp = top;
		data = top->data;
		top = top->next;
		free(temp);
		return data;
	}
}

//get element from front of queue
int front(){
    if(top == NULL){
        printf("Underflow\n");
        return 0;
    }
    else{
        return top->data;
    }
}

//get element from back of queue
int back(){
    if(top == NULL){
        printf("Underflow\n");
        return 0;
    }
    else{
        struct node *temp;
        temp = top;
        while(temp->next != NULL){
            temp = temp->next;
        }
        return temp->data;
    }
}

void display(){
	struct node *temp;
	temp = top;
	if(temp == NULL){
		printf("Stack is empty\n");
		return;
	}
	while(temp != NULL){
		printf("%d\n", temp->data);
		temp = temp->next;
	}
}

//get if queue is empty
bool isEmpty(){
    if(top == NULL){
        return true;
    }
    else{
        return false;
    }
}

//clear the queue
void clear(){
    struct node *temp;
    while(top != NULL){
        temp = top;
        top = top->next;
        free(temp);
    }
}
