using System;

namespace GeometryApp
{
    public class Circle : GeometricFigure  // ← УБРАЛ , IPrint
    {
        public double Radius { get; set; }

        public Circle(double radius)
        {
            Radius = radius;
        }

        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }

        public override string ToString()
        {
            return string.Format("Круг (Радиус {0}), {1}", Radius, base.ToString());
        }
        // УБРАЛ метод Print() - теперь использует наследование
    }
}
