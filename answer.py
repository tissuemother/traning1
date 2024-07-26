def solution(genres, plays):
    answer = []
    class music:
        def __init__(self,genres):
            self.genres = genres
            self.first_index = -1
            self.second_index = -1
            self.dict={}
        def push(self,plays,i):
            self.dict[i]=plays
            if self.first_index == -1:
                self.first_index = i
                self.second_index = i
            else:
                if plays>self.dict[self.first_index]:
                    tmp = self.first_index
                    self.first_index = i
                    self.second_index = tmp
                elif plays == self.dict[self.first_index]:
                    if i<self.first_index:
                        tmp= self.first_index
                        self.first_index = i
                        self.second_index = tmp
                    else:
                        self.second_index = i
                elif self.dict[self.first_index]>plays:
                    if self.first_index==self.second_index:
                        self.second_index = i
                    elif plays>self.dict[self.second_index]:
                        self.second_index = i
                    
                elif self.dict[self.second_index] == plays:
                    if i<self.second_index:
                        self.second_index = i
                
    genres_dict = {}
    for i in range(len(plays)):
        if genres[i] not in genres_dict.keys():
            genres_dict[genres[i]] = plays[i]
        else:
            genres_dict[genres[i]]+=plays[i]
    genres_dict = {k: v for k, v in sorted(genres_dict.items(), key=lambda item: item[1])[::-1]}
    for k in genres_dict.keys():
        mu = music(k)
        for i in range(len(plays)):
            if genres[i] == k:
                mu.push(plays[i],i)
        if mu.second_index == mu.first_index:
            answer.append(mu.first_index)
        else:
            answer.append(mu.first_index)
            answer.append(mu.second_index)
    
    return answer
