using System;

namespace GeometryApp
{
    public class SimpleList<T> where T : IComparable<T>
    {
        protected class Node
        {
            public T Data;
            public Node? Next;
            public Node(T data) { Data = data; Next = null; }
        }

        protected Node? head;
        public int Count { get; protected set; }

        public virtual void Add(T element)
        {
            Node newNode = new Node(element);
            newNode.Next = head;
            head = newNode;
            Count++;
        }

        public void Sort()
        {
            if (head == null || head.Next == null) return;

            bool swapped;
            do
            {
                swapped = false;
                Node? current = head;
                Node? previous = null;

                while (current != null && current.Next != null)
                {
                    if (current.Data.CompareTo(current.Next.Data) > 0)
                    {
                        T temp = current.Data;
                        current.Data = current.Next.Data;
                        current.Next.Data = temp;
                        swapped = true;
                    }
                    previous = current;
                    current = current.Next;
                }
            } while (swapped);
        }

        public override string ToString()
        {
            Node? current = head;
            string result = "";
            while (current != null)
            {
                result += current.Data + Environment.NewLine;
                current = current.Next;
            }
            return result;
        }
    }
}
