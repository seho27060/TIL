package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.StageReqDTO;
import com.practice.prac1.Domain.DTO.StageResDTO;

public interface StageService {

    StageResDTO saveStage(StageReqDTO stageReqDTO);

    StageResDTO readStage(Long index);

    StageResDTO updateStage(Long index,StageReqDTO stageReqDTO);

    Long deleteStage(Long index);
}
