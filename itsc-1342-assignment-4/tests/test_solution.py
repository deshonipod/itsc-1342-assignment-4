# DeShon Harris - Assignment 4 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import check_session

# Test 1: Well under default threshold (30 minutes)
assert check_session(10) == "SESSION_ACTIVE", "Failed Test 1"

# Test 2: Exactly at default threshold (30 minutes) should be expired
assert check_session(30) == "SESSION_EXPIRED", "Failed Test 2"

# Test 3: Well over default threshold
assert check_session(45) == "EXPIRED_SESSION", "Failed Test 3: Check return string value"

# Test 4: Custom threshold passed as argument
assert check_session(25, max_idle=20) == "SESSION_EXPIRED", "Failed Test 4"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 4")