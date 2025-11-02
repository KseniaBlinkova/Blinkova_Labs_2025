using System;

namespace GeometryApp
{
    public class Circle : GeometricFigure, IPrint
    {
        public double Radius { get; set; }

        public Circle(double Radius)
        {
            this.Radius = Radius;
        }

        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }

        public override string ToString()
        {
            return $"Круг: радиус = {Radius}, площадь = {Area():F2}";
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
