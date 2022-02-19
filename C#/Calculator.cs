using System;

//Note: Save to not get error's

namespace Program{

    class Calculator    
    { 
        static void Main()
        {
            Console.WriteLine("\nCalculator");
            Console.WriteLine("Add: +");
            Console.WriteLine("Subtract: -\n");

            Console.WriteLine("Divide: /");
            Console.WriteLine("Multiply: *");

    
            bool kn = false;
            while(kn == false){

                try{

                    Console.WriteLine("\nFirst Number: ");

                    int n1 = int.Parse(Console.ReadLine());

                    Console.WriteLine("Operator ()");
                    string oper = Console.ReadLine();

                    Console.WriteLine("Second Number: ");
                    int n2 = int.Parse(Console.ReadLine());

                    switch(oper){

                    case "+":
                    Console.WriteLine("");
                    Console.WriteLine(n1+n2);
                    break;

                    case "/":
                    Console.WriteLine("");
                    Console.WriteLine(n1/n2);
                    break;

                    case "-":
                    Console.WriteLine("");
                    Console.WriteLine(n1-n2);
                    break;

                    case "*":
                    Console.WriteLine("");
                    Console.WriteLine(n1*n2);
                    break;

                }
                }

                catch{
                    Console.WriteLine("Invalid Number(s)");
                }
                
        }
    }
    }

}

