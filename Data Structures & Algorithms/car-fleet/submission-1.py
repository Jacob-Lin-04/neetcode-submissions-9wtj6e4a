class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        # sort cars by position in decending order closest to target
        car_list = sorted(zip(position, speed), reverse = True)
        
        arrival_times = []
        
        for car in car_list:

            time = (target - car[0]) / car[1]

            #compare current cars time to previous fleets time
            if not arrival_times or time > arrival_times[-1]:
                arrival_times.append(time)
               

        return len(arrival_times)
        