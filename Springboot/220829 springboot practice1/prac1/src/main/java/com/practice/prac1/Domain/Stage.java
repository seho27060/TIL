package com.practice.prac1.Domain;

import com.practice.prac1.Domain.DTO.StageReqDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Stage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String content;

    private Integer level;

    @OneToMany(mappedBy = "stage", cascade = CascadeType.REMOVE)
    private List<MemberStage> memberStages;

    @OneToMany(mappedBy = "stage", cascade = CascadeType.REMOVE)
    private List<Post> postList;


    public void updateStage(StageReqDTO stageReqDTO){
        this.content = stageReqDTO.getContent();
        this.level = stageReqDTO.getLevel();
        this.title = stageReqDTO.getTitle();
    }
}
