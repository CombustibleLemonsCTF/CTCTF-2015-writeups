# CTCTF 2015: Javatar

### Problem

**Points**: 40

**Description**: 

> C++, JavaScript, Python, Java. Long ago four languages worked together then, everything changed when annoying developers started complaining. Only the Javatar can master all four languages.
Javatar

**Hint**: 

> Check out jd-gui

### Solution

Java, unlike other languages, is very friendly towards decompilers, such as [`jd-gui`](http://jd.benow.ca/), which is mentioned in the hint. After we downloaded `jd-gui` as well as some graphics libraries needed to run it, we got [this source](Javatar.java): 

```java
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
```

A complete understanding of the program is not even necessary to solve this challenge. We got the flag by running the code in the `if` block by passing in `WHOISTHEJAVATAR` as the first additional argument.

```
[!] mv Javatar.class JavatarOriginal.class
[!] javac Javatar.java
[!] java Javatar WHOISTHEJAVATAR
KELVINISTHEJAVATAR
```

Note: We had to store the original `Javatar.class` in `JavatarOriginal.class` and to recompile the program because of conflicting Java versions.

**Flag**: `KELVINISTHEJAVATAR`

### Other Resources

* None.
