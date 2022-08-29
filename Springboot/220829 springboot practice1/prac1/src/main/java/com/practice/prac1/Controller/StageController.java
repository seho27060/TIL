package com.practice.prac1.Controller;

import com.practice.prac1.Domain.DTO.StageReqDTO;
import com.practice.prac1.Domain.DTO.StageResDTO;
import com.practice.prac1.Domain.Stage;
import com.practice.prac1.Service.StageService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/stage")
@RequiredArgsConstructor
public class StageController {

    private final StageService stageService;

    @PostMapping("/save")
    public StageResDTO saveStage(@RequestBody StageReqDTO stageReqDTO){ return stageService.saveStage(stageReqDTO);}

    @GetMapping("/read/{index}")
    public StageResDTO readStage(@PathVariable("index") Long index){return stageService.readStage(index);}

    @PutMapping("/update/{index}")
    public StageResDTO updateStage(@PathVariable("index") Long index, StageReqDTO stageReqDTO){return stageService.updateStage(index,stageReqDTO);}

    @DeleteMapping("/delete/{index}")
    public Long deleteStage(@PathVariable("index") Long index){return stageService.deleteStage(index);}
}
