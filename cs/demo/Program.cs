using System;

namespace demo
{
    class Program
    {
        static void Main(string[] args)
        {
            Hello();
            Demo(true);
            Demo(false);
            Factorial(10);
        }

        private static void Hello()
        {
            Console.WriteLine("Hello World");
        }

        private static void Demo(bool parameter)
        {
            if (parameter)
            {
                Console.WriteLine("One");
            }
            else
            {
                Console.WriteLine("Two");
            }
        }

        private static void Factorial(int n)
        {
            var result = 1;
            for (; n > 0; n--)
            {
                result = result * n;
            }

            Console.WriteLine(result);
        }
    }
}
