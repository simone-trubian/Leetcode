def myAtoi(s: str) -> int:
        minus = False
        # Remove trailing spaces
        s = s.lstrip()
        
        # Capture sign if present
        if s.startswith("-"):
            minus = True
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        
        if len(s) == 0:
            return 0
        elif not s[0].isdigit():
            return 0
        elif s.isdigit():
           num = int(s) 
        else:
            for idx, char in enumerate(s):
                if not char.isdigit():
                    break
        
            num = int(s[:idx])
        
        if minus:
            num = -num

        if num<-2**31:
            return -2**31
        elif num>2**31 - 1:
            return 2**31 - 1
        else:
            return num