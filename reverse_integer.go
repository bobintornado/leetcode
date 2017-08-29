import "math"

func reverse(x int) int {
    negative := false
    if x < 0 {
        negative = true
        x = 0 - x
    }
    
    res := 0
    
    for x > 0 {
        mod := x % 10
        x = x / 10
        res = res * 10 + mod
    }
    
    if negative {
        res = 0 - res
    }
    
    if res > math.MaxInt32 || res < math.MinInt32 {
        return 0
    }
    
    return res
}
