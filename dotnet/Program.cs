using System;
using System.Collections;
using System.Collections.Generic;

namespace GeometryApp
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Лабораторная работа №6 - Работа с коллекциями");

            // 1. ArrayList
            Console.WriteLine("1. Работа с ArrayList:");
            ArrayList arrayList = new ArrayList();
            arrayList.Add(new Rectangle(5, 3));
            arrayList.Add(new Square(4));
            arrayList.Add(new Circle(2.5));
            arrayList.Add(new Rectangle(2, 6));
            arrayList.Add(new Circle(1.8));

            Console.WriteLine("Содержимое ArrayList (без сортировки):");
            foreach (GeometricFigure fig in arrayList)
            {
                Console.WriteLine(fig);
            }

            // 2. List<GeometricFigure>
            Console.WriteLine("\n2. Работа с List<GeometricFigure>:");
            List<GeometricFigure> list = new List<GeometricFigure>();
            list.Add(new Rectangle(5, 3));
            list.Add(new Square(4));
            list.Add(new Circle(2.5));
            list.Add(new Rectangle(2, 6));
            list.Add(new Circle(1.8));

            Console.WriteLine("До сортировки:");
            foreach (var fig in list)
            {
                Console.WriteLine(fig);
            }

            list.Sort();

            Console.WriteLine("\nПосле сортировки:");
            foreach (var fig in list)
            {
                Console.WriteLine(fig);
            }

            // 3. SimpleStack
            Console.WriteLine("3. Работа со стеком:");
            SimpleStack<GeometricFigure> stack = new SimpleStack<GeometricFigure>();

            stack.Push(new Rectangle(4, 5));
            stack.Push(new Square(3));
            stack.Push(new Circle(2));
            stack.Push(new Rectangle(6, 2));

            Console.WriteLine("Содержимое стека после добавления элементов:");
            Console.WriteLine(stack);

            Console.WriteLine("\nИзвлечение элементов из стека:");
            while (!stack.IsEmpty())
            {
                GeometricFigure figure = stack.Pop();
                Console.WriteLine("Извлечен: " + figure);
            }

            // 4. Демонстрация сортировки в SimpleList
            Console.WriteLine("\n4. Демонстрация сортировки в SimpleList:");
            SimpleList<GeometricFigure> simpleList = new SimpleList<GeometricFigure>();
            simpleList.Add(new Rectangle(4, 5));
            simpleList.Add(new Square(3));
            simpleList.Add(new Circle(2));
            simpleList.Add(new Rectangle(6, 2));

            Console.WriteLine("До сортировки:");
            Console.WriteLine(simpleList);

            simpleList.Sort();

            Console.WriteLine("После сортировки:");
            Console.WriteLine(simpleList);

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
