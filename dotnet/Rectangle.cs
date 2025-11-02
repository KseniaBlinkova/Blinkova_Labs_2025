using System;

namespace GeometryApp
{
    public class Rectangle : GeometricFigure, IPrint
    {
        public double Width { get; set; }
        public double Height { get; set; }

        public Rectangle(double Width, double Height)
        {
            this.Width = Width;
            this.Height = Height;
        }

        public override double Area()
        {
            return Width * Height;
        }

        public override string ToString()
        {
            return $"Прямоугольник: ширина = {Width}, высота = {Height}, площадь = {Area():F2}";
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
