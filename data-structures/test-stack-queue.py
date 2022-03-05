"""
Test linked list implementation of stack and queue data structures
"""
from stack import *
from queue import *


def main():
	#PART 1: Queues
	#Step-01: Build a new queue.
	queue1 = Queue(4)

	#STEP-02: Print result of isEmpty()/full()
	print("=== Testing Queue ===")
	print("Test 1: Queue Empty/Full")
	print("Result: ", queue1.isEmpty(), " - ", queue1.isFull())
	print()

	#Step-03: Push values into Queue
	print("Test 2: Enqueueing nodes until full.")
	print("Result: ", queue1.enqueue(4))
	print("Result: ", queue1.enqueue(3))
	print("Result: ", queue1.enqueue(2))
	print("Result: ", queue1.enqueue(1))
	print("Result: ", queue1.enqueue(0))
	print()

	#STEP-04: Peek at the top/empty Full
	print("Test 3: Queue front and Empty/Full")
	print("Result: ", queue1.isEmpty(), " - ", queue1.isFull())
	print("The value at the front of the queue is: ", queue1.front())
	print()

	#Step-05: Dequeue and print
	print("Test 4: dequeueing values until empty.")
	temp = queue1.dequeue()
	print(temp)
	temp = queue1.dequeue()
	print(temp)
	temp = queue1.dequeue()
	print(temp)
	temp = queue1.dequeue()
	print(temp)
	temp = queue1.dequeue()
	if(temp == False):
		print("Queue Empty: Dequeue Failed")
	else:
		print("Something went wrong here...")

	print("Queue empty/full result: ", queue1.isEmpty(), " - ", queue1.isFull())
	print("==== End Testing ====")
	print("\n")

	#Part 2: Stack
	#Step-01: Build a new stack
	stack1 = Stack(4)

	#Step-02: print isEmpty/full
	print("=== Testing Stack ===")
	print("Test 1: Stack Empty/Full")
	print("Result: ", stack1.isEmpty(), " - ", stack1.isFull())
	print()

	#Step-03: Push values into Stack
	print("Test 2: Pushing values until full.")
	print("Result: ", stack1.push(1))
	print("Result: ", stack1.push(2))
	print("Result: ", stack1.push(3))
	print("Result: ", stack1.push(4))
	print("Result: ", stack1.push(1))
	print()

	#STEP-04: Peek at the top/empty Full
	print("Test 3: Stack peek and Empty/Full")
	print("Result: ", stack1.isEmpty(), " - ", stack1.isFull())
	temp = stack1.peek()
	print("The value at the top of the stack is: ", temp)
	print()

    #Step-05: pop and print
	print("Test 4: Popping values until empty.")
	temp = stack1.pop()
	print(temp)
	temp = stack1.pop()
	print(temp)
	temp = stack1.pop()
	print(temp)
	temp = stack1.pop()
	print(temp)
	temp = stack1.pop()
	if(temp == False):
		print("Stack Empty: Pop Failed")
	else:
		print("Something went wrong here...")
	print("Stack empty/full result: ", stack1.isEmpty(), " - ", stack1.isFull())

	return True


if __name__ == "__main__":
    main()
