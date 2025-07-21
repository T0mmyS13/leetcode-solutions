using System;
public class Solution

{
    public string MakeFancyString(string s)
    {


        if (s.Length < 3)
        {
            return s;
        }
        var result = new System.Text.StringBuilder();
        result.Append(s[0]);
        result.Append(s[1]);
        for (int i = 2; i < s.Length; i++)
        {
            if (!(s[i] == s[i - 1] && s[i] == s[i - 2]))
            {
                result.Append(s[i]);
            }
        }
        return result.ToString();

    }
}
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine(new Solution().MakeFancyString("leeetcode"));
    }
}

