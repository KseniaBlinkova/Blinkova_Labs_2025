using System;

namespace GeometryApp
{
    public abstract class GeometricFigure : IComparable<GeometricFigure>
    {
        public abstract double Area();

        public int CompareTo(GeometricFigure? other)
        {
            if (other == null) return 1;
            return this.Area().CompareTo(other.Area());
        }

        public override string ToString()
        {
            return string.Format("Площадь = {0:F2}", Area());
        }

        public virtual void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
}
