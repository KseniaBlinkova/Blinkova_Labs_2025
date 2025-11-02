using System;

namespace GeometryApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Геометрические фигуры");

            Rectangle rectangle = new Rectangle(5, 3);
            Square square = new Square(4);
            Circle circle = new Circle(2.5);

            Console.WriteLine("Информация о фигурах (через Print):");
            rectangle.Print();
            square.Print();
            circle.Print();

            Console.WriteLine("\nИнформация о фигурах (через ToString):");
            Console.WriteLine(rectangle.ToString());
            Console.WriteLine(square.ToString());
            Console.WriteLine(circle.ToString());

            Console.WriteLine("\nДемонстрация полиморфизма:");

            GeometricFigure[] figures = new GeometricFigure[]
            {
                new Rectangle(6, 2),
                new Square(3),
                new Circle(1.5)
            };

            foreach (var figure in figures)
            {
                Console.WriteLine($"Площадь фигуры: {figure.Area():F2}");
            }

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
