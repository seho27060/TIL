package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.StageReqDTO;
import com.practice.prac1.Domain.DTO.StageResDTO;
import com.practice.prac1.Domain.Stage;
import com.practice.prac1.Repository.StageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
public class StageServiceImpl implements StageService{

    private final StageRepository stageRepository;

    @Override
    public StageResDTO saveStage(StageReqDTO stageReqDTO) {
        Stage stage = Stage.builder()
                .title(stageReqDTO.getTitle())
                .level(stageReqDTO.getLevel())
                .content(stageReqDTO.getContent())
                .build();
        Stage innerStage = stageRepository.save(stage);
        StageResDTO stageResDTO = StageResDTO.builder()
                .id(innerStage.getId())
                .title(innerStage.getTitle())
                .level(innerStage.getLevel())
                .content(innerStage.getContent())
                .build();
        return stageResDTO;
    }

    @Override
    public StageResDTO readStage(Long index) {
        Optional<Stage> stage = stageRepository.findById(index);
        if (stage.isPresent()){
            Stage innerStage = stage.get();
            StageResDTO stageResDTO = StageResDTO.builder()
                    .title(innerStage.getTitle())
                    .level(innerStage.getLevel())
                    .id(innerStage.getId())
                    .content(innerStage.getContent())
                    .build();
            return stageResDTO;
        }
        return null;
    }

    @Override
    public StageResDTO updateStage(Long index, StageReqDTO stageReqDTO) {
        Optional<Stage> stage = stageRepository.findById(index);
        
        if(stage.isPresent()){
            Stage innerStage = stage.get();
            innerStage.updateStage(stageReqDTO);
            StageResDTO stageResDTO = StageResDTO.builder()
                    .id(innerStage.getId())
                    .title(innerStage.getTitle())
                    .level(innerStage.getLevel())
                    .content(innerStage.getContent())
                    .build();
            return stageResDTO;
        }
        return null;
    }

    @Override
    public Long deleteStage(Long index) {
        Optional<Stage> stage = stageRepository.findById(index);
        if (stage.isPresent()){
            stageRepository.deleteById(index);
            return index;
        }
        return null;
    }
}
