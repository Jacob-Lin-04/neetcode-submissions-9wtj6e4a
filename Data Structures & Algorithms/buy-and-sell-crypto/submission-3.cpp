class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Keep track of the minimum price and maximum profit
        int minPrice = 100;
        int maxProfit = 0;

        for (int price : prices){
            minPrice = min(price, minPrice);
            
            int profit = (price - minPrice);

            if (profit > maxProfit) {
                maxProfit = profit;

            }

        }
        
        return maxProfit;

    }
};
