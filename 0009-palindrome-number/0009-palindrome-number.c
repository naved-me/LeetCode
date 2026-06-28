bool isPalindrome(int x) {
    long long int result=0,temp;
    temp=x;  // temp is used to stores the original value of 
            //x before x gets modified during reversal.

    if(x<0)
    {
        return false;  //checking the number is negative or not
    }

    while(x!=0)
    {
        
        result=result*10+(x%10);  // This use to reverse the number
        x/=10;
        
    }

  if(result!=temp)
  {
    return false;  // checking wheater the resultant number 
                   // is equal to given number or not then return false
  }
 return true;
}