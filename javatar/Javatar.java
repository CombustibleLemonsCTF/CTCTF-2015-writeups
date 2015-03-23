import java.io.PrintStream;

public class Javatar
{
  public static void main(String[] paramArrayOfString)
  {
    String str1 = "KYLIIWIBTKEQAAAOAW";
    String str2 = "PEQVVNRSAHFJKVWTLR";
    String str3;
    int i;
    if (paramArrayOfString[0].equals("WHOISTHEJAVATAR")) {
      str3 = "";
      for (i = 0; i < str1.length(); i++) {
        if (i % 2 == 0) str3 = str3 + str1.charAt(i); else
          str3 = str3 + str2.charAt(i);
      }
      System.out.println(str3);
    }
    else
    {
      str3 = "";
      for (i = 0; i < str1.length(); i++) {
        if (i % 2 != 0) str3 = str3 + str1.charAt(i); else
          str3 = str3 + str2.charAt(i);
      }
      System.out.println(str3);
    }
  }
}