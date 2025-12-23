using System;

namespace GeometryApp
{
    public class SimpleStack<T> : SimpleList<T> where T : IComparable<T>
    {
        public void Push(T element)
        {
            Add(element);
        }

        public T Pop()
        {
            if (head == null) throw new InvalidOperationException("Стек пуст");
            T value = head!.Data;
            head = head!.Next;
            Count--;
            return value;
        }

        public T Peek()
        {
            if (head == null) throw new InvalidOperationException("Стек пуст");
            return head!.Data;
        }

        public bool IsEmpty()
        {
            return head == null;
        }
    }
}
