using System;

namespace GeometryApp
{
    public class Square : Rectangle, IPrint
    {
        public Square(double Side) : base(Side, Side)
        {
        }

        public override string ToString()
        {
            return $"Квадрат: сторона = {Width}, площадь = {Area():F2}";
        }
    }
}
