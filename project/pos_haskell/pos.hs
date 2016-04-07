import Data.Time.Clock
import Data.Time.Calendar

-- Define a constant Float called taxRate as 0.065
taxRate :: Double
taxRate = 0.065

-- anonymous function '\' returns a list
-- mapped to string -> i
digitize :: Integer -> [Int]
digitize nt = map() (show nt)

stringsToIntegers :: [String] -> [Integer]
stringsToIntegers x = read [x] :: Int

cardType :: Integer -> String
cardType x | (head (digitize x)) == 4 = "Visa"
           | (head (digitize x)) == 5 = "MasterCard"
           | (head (digitize x)) == 6 = "Discover"
           | otherwise = "Not Accepted"

-- pastDate :: Integer -> date -> Int -> IO Bool
-- pastDate year month day = (\)
-- pastDate
-- pastDate :: Integer -> date
-- pastDate :: (Integer, Int, Int) -> Bool
-- pastDate year month day =

date :: IO (Integer, Int, Int) -- :: (year,month,day)
date = getCurrentTime >>= return . toGregorian . utctDay
