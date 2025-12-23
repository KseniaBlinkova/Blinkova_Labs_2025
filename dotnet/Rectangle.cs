using System;

namespace GeometryApp
{
    public class Rectangle : GeometricFigure  // ← УБРАЛ , IPrint
    {
        public double Width { get; set; }
        public double Height { get; set; }

        public Rectangle(double width, double height)
        {
            Width = width;
            Height = height;
        }

        public override double Area()
        {
            return Width * Height;
        }

        public override string ToString()
        {
            return string.Format("Прямоугольник (Ш {0}, В {1}), {2}", Width, Height, base.ToString());
        }
        // УБРАЛ метод Print() - теперь использует наследование
    }
}
