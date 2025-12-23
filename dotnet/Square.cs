using System;

namespace GeometryApp
{
    public class Square : GeometricFigure  // ← УБРАЛ , IPrint
    {
        public double Side { get; set; }

        public Square(double side)
        {
            Side = side;
        }

        public override double Area()
        {
            return Side * Side;
        }

        public override string ToString()
        {
            return string.Format("Квадрат (Сторона {0}), {1}", Side, base.ToString());
        }
        // УБРАЛ метод Print() - теперь использует наследование
    }
}
