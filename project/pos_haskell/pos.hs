import Data.Time.Clock
import Data.Time.Calendar

-- Define a constant Float called taxRate as 0.065
taxRate :: Double
taxRate = 0.065

digitize :: Integer -> [Integer]
digitize 0 = []
digitize x = digitize (x `div` 10) ++ [x `mod` 10]

cardType :: Integer -> String
cardType x | (head (digitize x)) == 4 = "Visa"
           | (head (digitize x)) == 5 = "MasterCard"
           | (head (digitize x)) == 6 = "Discover"
           | otherwise = "Not Accepted"

pastDate :: Integer -> Int -> Int -> Bool
pastDate cardYear cardMonth cardDay
    | cardYear > year = True
    | cardMonth > month = True
    | cardDay > day = True
    | otherwise = False
    where
      (year, month, day) =  date

date :: IO (Integer, Int, Int) -- :: (year,month,day)
date = fmap (toGregorian . utctDay) getCurrentTime
